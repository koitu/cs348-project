
import React, { useEffect, useParams, useState } from "react"

export function TeamDetailedPage() {
    let { id } = useParams()
    return (
        <p>
            this is detailed webpage for team with {id}
        </p>
    )
}